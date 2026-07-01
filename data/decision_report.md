# Decision Report

- generated_at: 2026-07-01T20:00:18.945438+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8010**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8010, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.31% | **-0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +3.09% | **+0.77%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.91% | **+0.69%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.77% | **+0.48%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.47% | **+0.44%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.13% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.30% | **+1.30%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.99% | **+0.70%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| ASK_LONG | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +0.77% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$275.09** / 初期 $100.00 (+175.09%)
- 確定: 2407件 (Win 736 / Loss 797 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIF/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $275.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.42** / 初期 $100.00 (+7.42%)
- 確定: 527件 (Win 134 / Loss 124 / Flat 269) / skip 894件
- 成長率目線: 平均log +0.000136 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0380 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $107.42

## 5. Latest Market Context

- 更新: 2026-07-01T20:00:14.009180+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=59989.9
- Funnel: target 825 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NOM/USDT:USDT | +21.54% | $4,311,149.79 |
| RIF/USDT:USDT | +16.43% | $2,801,109.59 |
| LIT/USDT:USDT | +12.29% | $4,791,878.87 |
| VELVET/USDT:USDT | +9.32% | $28,023,290.90 |
| TAIKO/USDT:USDT | +6.11% | $20,387,739.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.13% | +3.39% |
| BEAT/USDT:USDT | below_1h_threshold | +1.82% | +2.07% |
| XMR/USDT:USDT | below_1h_threshold | +0.89% | +1.14% |
| CRV/USDT:USDT | below_1h_threshold | +0.72% | +0.97% |
| NIOSTOCK/USDT:USDT | below_1h_threshold | +0.10% | +0.36% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
