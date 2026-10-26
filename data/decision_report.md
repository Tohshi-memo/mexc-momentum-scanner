# Decision Report

- generated_at: 2026-10-26T22:26:32.124348+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17524**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.40% / filled 20/20。**
- 全期間 MARKET基準: n=17524, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 9/20 | 45.0% | +2.85% | **+1.28%** |
| LIMIT_9PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_BB3S | 3/10 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_8PCT | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.43% | **+2.07%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.59% | **+1.51%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.96% | **+1.47%** |
| LIMIT_BB3S_LONG | 5/10 | 50.0% | +2.75% | **+1.37%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 252件 (TP 93 / SL 151 / EXP 8)
- 最新: Q/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,526.92** / 初期 $100.00 (+1426.92%)
- 確定: 6721件 (Win 1956 / Loss 2152 / Flat 2613) / skip 7364件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,526.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$318.99** / 初期 $100.00 (+218.99%)
- 確定: 4053件 (Win 1116 / Loss 952 / Flat 1985) / skip 6882件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0647 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MRNASTOCK/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $318.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5688件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000320 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T22:26:19.401216+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=79955.6
- Funnel: target 1078 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +184.10% | $16,406,904.83 |
| DODO/USDT:USDT | +7.11% | $1,355,831.43 |
| AGT/USDT:USDT | +6.16% | $1,719,324.35 |
| DNA/USDT:USDT | +3.14% | $1,204,589.63 |
| ORDER/USDT:USDT | +2.73% | $1,119,886.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRYS/USDT:USDT | below_1h_threshold | +4.33% | +4.48% |
| ORDER/USDT:USDT | below_1h_threshold | +3.48% | +3.63% |
| DODO/USDT:USDT | below_1h_threshold | +3.25% | +3.40% |
| AGT/USDT:USDT | below_1h_threshold | +2.13% | +2.27% |
| SNXX/USDT:USDT | below_1h_threshold | +0.71% | +0.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
