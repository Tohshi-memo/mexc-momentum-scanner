# Decision Report

- generated_at: 2026-08-09T09:36:30.167209+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10993**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.60% / filled 20/20。**
- 全期間 MARKET基準: n=10993, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.89% | **+1.61%** |
| LIMIT_BB3S | 7/19 | 36.8% | +4.00% | **+1.47%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.83% | **+0.54%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.13% | **+0.53%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.34% | **+0.18%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$628.11** / 初期 $100.00 (+528.11%)
- 確定: 3931件 (Win 1230 / Loss 1281 / Flat 1420) / skip 3623件
- 成長率目線: 平均log +0.000467 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XAI/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $628.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1512件 (Win 424 / Loss 360 / Flat 728) / skip 2892件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_8PCT` (selected_by_robust_growth_score) / robust_score +0.1068 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.44** / 初期 $100.00 (+17.44%)
- 確定: 1248件 (Win 390 / Loss 480 / Flat 378) / pending 0件 / skip 1224件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000256 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.10% 残高後 $117.44

## 6. Latest Market Context

- 更新: 2026-08-09T09:36:17.659517+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64779.8
- Funnel: target 961 → liquid 153 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.7 >= 65=1, 4h RSI 90.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +139.94% | $62,733,681.88 |
| BMT/USDT:USDT | +77.12% | $2,055,011.74 |
| MUBARAK/USDT:USDT | +32.79% | $2,035,255.39 |
| COOKIE/USDT:USDT | +25.97% | $4,981,869.58 |
| IOTX/USDT:USDT | +25.51% | $6,014,835.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLUAI/USDT:USDT | below_1h_threshold | +4.16% | +4.18% |
| COOKIE/USDT:USDT | below_1h_threshold | +3.37% | +3.39% |
| CASHCAT/USDT:USDT | below_1h_threshold | +3.00% | +3.02% |
| XAI/USDT:USDT | below_1h_threshold | +2.51% | +2.53% |
| BEAT/USDT:USDT | below_1h_threshold | +2.22% | +2.24% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
