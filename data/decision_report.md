# Decision Report

- generated_at: 2026-09-01T18:56:38.090495+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13257**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13257, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.72% | **-0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.77% | **+0.53%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.99% | **+0.45%** |
| LIMIT_6PCT | 4/20 | 20.0% | +2.03% | **+0.41%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.03% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.07% | **+0.91%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.55% | **+0.36%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.85% | **+0.30%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.42% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$788.73** / 初期 $100.00 (+688.73%)
- 確定: 4892件 (Win 1488 / Loss 1614 / Flat 1790) / skip 4926件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: USELESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $788.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.59** / 初期 $100.00 (+73.59%)
- 確定: 2236件 (Win 623 / Loss 539 / Flat 1074) / skip 4432件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0669 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $173.59

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.08** / 初期 $100.00 (+15.08%)
- 確定: 2088件 (Win 610 / Loss 816 / Flat 662) / pending 1件 / skip 2642件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000155 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.08

## 6. Latest Market Context

- 更新: 2026-09-01T18:56:26.005738+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=76919.7
- Funnel: target 1036 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.3 >= 65=1, 4h RSI 84.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +13.21% | $5,026,300.20 |
| USELESS/USDT:USDT | +12.28% | $36,024,988.77 |
| MAGMA/USDT:USDT | +8.59% | $1,895,229.31 |
| FILECOIN/USDT:USDT | +6.84% | $9,153,830.52 |
| UAI/USDT:USDT | +6.20% | $4,931,216.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.91% | +5.32% |
| MAGMA/USDT:USDT | below_1h_threshold | +4.59% | +5.01% |
| SOXS/USDT:USDT | below_1h_threshold | +1.48% | +1.90% |
| DOS/USDT:USDT | below_1h_threshold | +1.08% | +1.49% |
| BICO/USDT:USDT | below_1h_threshold | +1.02% | +1.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
