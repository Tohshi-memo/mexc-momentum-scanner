# Decision Report

- generated_at: 2026-10-23T02:06:32.787580+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17179**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.52% / filled 20/20。**
- 全期間 MARKET基準: n=17179, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.52% | **+1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.52% | **+1.52%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.20% | **+1.08%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.92% | **+0.73%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_BB3S | 3/19 | 15.8% | +1.47% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.94% | **+0.42%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.35% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,336.00** / 初期 $100.00 (+1236.00%)
- 確定: 6536件 (Win 1898 / Loss 2084 / Flat 2554) / skip 7204件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $1,336.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.86** / 初期 $100.00 (+177.86%)
- 確定: 3856件 (Win 1056 / Loss 899 / Flat 1901) / skip 6734件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0320 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $277.86

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5342件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000230 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T02:06:18.145626+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=81220.8
- Funnel: target 1096 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +63.85% | $10,662,724.51 |
| IRYS/USDT:USDT | +19.09% | $3,825,467.72 |
| AGT/USDT:USDT | +13.86% | $5,009,609.86 |
| DNA/USDT:USDT | +9.05% | $4,082,563.18 |
| DASH/USDT:USDT | +8.67% | $17,641,753.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +4.20% | +4.31% |
| BTW/USDT:USDT | below_1h_threshold | +1.15% | +1.27% |
| AKE/USDT:USDT | below_1h_threshold | +1.14% | +1.25% |
| USOIL/USDT:USDT | below_1h_threshold | +1.12% | +1.23% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.12% | +1.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
