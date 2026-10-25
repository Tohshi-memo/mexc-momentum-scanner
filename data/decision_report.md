# Decision Report

- generated_at: 2026-10-25T08:11:18.522785+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17412**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17412, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.34% | **-1.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 18/20 | 90.0% | +1.29% | **+1.17%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.55% | **+0.44%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.02% | **+0.25%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.53% | **+1.77%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.18% | **+1.75%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +4.18% | **+1.67%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.80% | **+1.54%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.85% | **+1.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,512.63** / 初期 $100.00 (+1412.63%)
- 確定: 6665件 (Win 1937 / Loss 2123 / Flat 2605) / skip 7308件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $1,512.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$310.71** / 初期 $100.00 (+210.71%)
- 確定: 3955件 (Win 1095 / Loss 927 / Flat 1933) / skip 6868件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1629 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $310.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5570件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000519 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-25T08:11:06.058892+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=80578.1
- Funnel: target 1071 → liquid 129 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| T/USDT:USDT | +32.99% | $4,688,611.94 |
| APR/USDT:USDT | +32.14% | $5,938,645.13 |
| AGT/USDT:USDT | +18.19% | $5,386,469.81 |
| USELESS/USDT:USDT | +17.37% | $4,343,405.59 |
| LIGHT/USDT:USDT | +15.39% | $1,414,756.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIGHT/USDT:USDT | below_1h_threshold | +4.54% | +4.62% |
| AGT/USDT:USDT | below_1h_threshold | +1.97% | +2.05% |
| MUU/USDT:USDT | below_1h_threshold | +0.65% | +0.74% |
| SNXX/USDT:USDT | below_1h_threshold | +0.61% | +0.70% |
| KORU/USDT:USDT | below_1h_threshold | +0.57% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
