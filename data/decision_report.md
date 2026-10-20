# Decision Report

- generated_at: 2026-10-20T09:56:35.537833+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17054**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17054, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.00% | **+0.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.10% | **+0.84%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.35% | **+0.50%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.45% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 9/9 | 100.0% | +2.05% | **+2.05%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.98% | **+1.48%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.63% | **+1.22%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.51% | **+1.21%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.51% | **+0.98%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,311.01** / 初期 $100.00 (+1211.01%)
- 確定: 6480件 (Win 1884 / Loss 2068 / Flat 2528) / skip 7135件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,311.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$280.30** / 初期 $100.00 (+180.30%)
- 確定: 3802件 (Win 1045 / Loss 886 / Flat 1871) / skip 6663件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $280.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5212件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000228 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-20T09:56:20.267161+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=81414.0
- Funnel: target 1078 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +83.23% | $6,031,787.27 |
| ALT/USDT:USDT | +17.97% | $1,719,500.36 |
| PHA/USDT:USDT | +16.67% | $18,992,845.16 |
| BAT/USDT:USDT | +11.79% | $7,439,140.68 |
| A/USDT:USDT | +11.25% | $23,249,488.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TIA/USDT:USDT | below_1h_threshold | +1.26% | +1.36% |
| BAT/USDT:USDT | below_1h_threshold | +0.92% | +1.02% |
| USOIL/USDT:USDT | below_1h_threshold | +0.91% | +1.02% |
| LIT/USDT:USDT | below_1h_threshold | +0.56% | +0.66% |
| JUP/USDT:USDT | below_1h_threshold | +0.47% | +0.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
