# Decision Report

- generated_at: 2026-11-27T23:51:34.407599+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19806**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19806, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.70% | **-1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_BB3S | 3/14 | 21.4% | -0.00% | **-0.00%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.53% | **-0.27%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -1.18% | **-0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +6.42% | **+3.21%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.38% | **+2.14%** |
| MARKET_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.41% | **+0.96%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.68% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$121.76** / 初期 $100.00 (+21.76%)
- 確定トレード: 292件 (TP 106 / SL 176 / EXP 10)
- 最新: SNXX/USDT:USDT EXPIRED PnL +2.62% 残高後 $121.76
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,961.21** / 初期 $100.00 (+1861.21%)
- 確定: 7649件 (Win 2201 / Loss 2461 / Flat 2987) / skip 8718件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,961.21

## 4. Robust Adaptive DryRun ($100)

- 残高: **$460.06** / 初期 $100.00 (+360.06%)
- 確定: 5297件 (Win 1410 / Loss 1141 / Flat 2746) / skip 7920件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0427 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $460.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7968件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000158 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-27T23:51:20.414959+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=59862.1
- Funnel: target 1101 → liquid 140 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +49.28% | $12,081,224.34 |
| ACE/USDT:USDT | +35.02% | $1,917,470.00 |
| SKY/USDT:USDT | +12.89% | $3,098,693.46 |
| VELVET/USDT:USDT | +10.19% | $5,400,448.80 |
| BTW/USDT:USDT | +7.91% | $8,456,152.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +1.89% | +1.64% |
| LTC/USDT:USDT | below_1h_threshold | +1.33% | +1.07% |
| SSV/USDT:USDT | below_1h_threshold | +1.09% | +0.84% |
| LIT/USDT:USDT | below_1h_threshold | +0.93% | +0.68% |
| STRK/USDT:USDT | below_1h_threshold | +0.89% | +0.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
