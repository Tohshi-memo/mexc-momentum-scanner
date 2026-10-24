# Decision Report

- generated_at: 2026-10-24T00:31:31.564454+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17305**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17305, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 12/20 | 60.0% | +3.96% | **+2.38%** |
| LIMIT_7PCT | 10/20 | 50.0% | +4.04% | **+2.02%** |
| LIMIT_8PCT | 8/20 | 40.0% | +4.46% | **+1.79%** |
| LIMIT_9PCT | 6/20 | 30.0% | +3.43% | **+1.03%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.86% | **+1.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +1.14% | **+0.80%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.80% | **+0.60%** |
| LIMIT_10PCT_LONG | 8/20 | 40.0% | +1.28% | **+0.51%** |
| LIMIT_9PCT_LONG | 9/20 | 45.0% | +1.13% | **+0.51%** |
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +0.76% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.62** / 初期 $100.00 (+1210.62%)
- 確定: 6559件 (Win 1903 / Loss 2096 / Flat 2560) / skip 7307件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BIRB/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $1,310.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3929件 (Win 1083 / Loss 920 / Flat 1926) / skip 6787件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1078 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5466件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000276 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-24T00:31:16.206512+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.43% price=80813.7
- Funnel: target 1088 → liquid 167 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.4 >= 65=1, 4h RSI 69.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIRB/USDT:USDT | +57.67% | $4,390,417.00 |
| IRYS/USDT:USDT | +30.35% | $96,110,062.69 |
| AGT/USDT:USDT | +27.17% | $10,824,419.70 |
| AXIS/USDT:USDT | +25.96% | $1,641,270.15 |
| SOXS/USDT:USDT | +4.50% | $31,825,500.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXIS/USDT:USDT | below_1h_threshold | +1.23% | +1.66% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +0.88% | +1.31% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.74% | +1.17% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.71% | +1.13% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.56% | +0.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
