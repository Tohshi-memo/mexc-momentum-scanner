# Decision Report

- generated_at: 2026-11-03T13:26:41.829930+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18085**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18085, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.19% | **-1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +2.57% | **+0.90%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +2.14% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.00% | **+3.00%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.46% | **+1.02%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.72% | **+0.94%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.06% | **+0.93%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.35% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 260件 (TP 96 / SL 156 / EXP 8)
- 最新: EVAA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,500.44** / 初期 $100.00 (+1400.44%)
- 確定: 6921件 (Win 2001 / Loss 2219 / Flat 2701) / skip 7725件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ICNT/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,500.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$379.73** / 初期 $100.00 (+279.73%)
- 確定: 4506件 (Win 1207 / Loss 1003 / Flat 2296) / skip 6990件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1147 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $379.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6247件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000248 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-03T13:26:26.750848+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=77330.0
- Funnel: target 1084 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +75.36% | $9,622,377.44 |
| IDOL/USDT:USDT | +44.32% | $14,371,444.95 |
| ICNT/USDT:USDT | +30.67% | $3,361,304.07 |
| HOT/USDT:USDT | +27.27% | $9,637,709.69 |
| UAI/USDT:USDT | +19.74% | $7,903,596.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.65% | +2.74% |
| RUNE/USDT:USDT | below_1h_threshold | +1.32% | +1.41% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.48% | +0.57% |
| UAI/USDT:USDT | below_1h_threshold | +0.32% | +0.41% |
| DNA/USDT:USDT | below_1h_threshold | +0.11% | +0.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
