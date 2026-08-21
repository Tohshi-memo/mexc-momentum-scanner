# Decision Report

- generated_at: 2026-08-21T22:51:25.112613+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12267**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12267, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.60% | **-0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_8PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_BB3S | 8/18 | 44.4% | +3.52% | **+1.56%** |
| LIMIT_6PCT | 5/20 | 25.0% | +5.55% | **+1.39%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.96% | **+2.18%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.30% | **+1.23%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.65% | **+1.08%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.11% | **+0.83%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$665.61** / 初期 $100.00 (+565.61%)
- 確定: 4387件 (Win 1343 / Loss 1438 / Flat 1606) / skip 4441件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $665.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.95** / 初期 $100.00 (+54.95%)
- 確定: 1874件 (Win 516 / Loss 448 / Flat 910) / skip 3804件
- 成長率目線: 平均log +0.000234 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0942 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $154.95

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1919件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000250 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T22:51:15.066397+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=78268.6
- Funnel: target 1018 → liquid 219 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.9 >= 65=1, 4h RSI 93.1 >= 65=1, 4h RSI 83.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +202.47% | $2,889,064.08 |
| CATE/USDT:USDT | +47.04% | $10,777,494.75 |
| JIMOTHY/USDT:USDT | +28.12% | $1,595,451.17 |
| AGI/USDT:USDT | +17.55% | $1,507,371.21 |
| BLESS/USDT:USDT | +14.97% | $10,481,476.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FLOKI/USDT:USDT | below_1h_threshold | +4.29% | +4.57% |
| AGI/USDT:USDT | below_1h_threshold | +3.95% | +4.23% |
| MONAD/USDT:USDT | below_1h_threshold | +3.64% | +3.93% |
| CC/USDT:USDT | below_1h_threshold | +2.99% | +3.27% |
| BLESS/USDT:USDT | below_1h_threshold | +2.83% | +3.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
