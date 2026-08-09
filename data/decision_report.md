# Decision Report

- generated_at: 2026-08-09T12:56:40.214592+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11024**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.18% / filled 20/20。**
- 全期間 MARKET基準: n=11024, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.13% | **+0.85%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.26% | **+0.18%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +1.04% | **+0.31%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.52% | **+0.28%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.85% | **+0.25%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.15% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$628.11** / 初期 $100.00 (+528.11%)
- 確定: 3931件 (Win 1230 / Loss 1281 / Flat 1420) / skip 3654件
- 成長率目線: 平均log +0.000467 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XAI/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $628.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1512件 (Win 424 / Loss 360 / Flat 728) / skip 2923件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0350 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.24** / 初期 $100.00 (+17.24%)
- 確定: 1259件 (Win 390 / Loss 481 / Flat 388) / pending 6件 / skip 1236件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000366 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATI/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $117.24

## 6. Latest Market Context

- 更新: 2026-08-09T12:56:20.473020+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64915.5
- Funnel: target 961 → liquid 152 → pre 50 → checked 50 → surge 5 → strict 4
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +118.69% | $70,711,728.43 |
| BMT/USDT:USDT | +83.80% | $5,388,145.36 |
| COOKIE/USDT:USDT | +35.72% | $6,095,032.30 |
| XAN/USDT:USDT | +28.52% | $3,842,655.36 |
| CATI/USDT:USDT | +22.30% | $3,201,357.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CYS/USDT:USDT | below_1h_threshold | +4.02% | +4.03% |
| MMT/USDT:USDT | below_1h_threshold | +2.45% | +2.46% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.29% | +2.30% |
| BEAT/USDT:USDT | below_1h_threshold | +1.91% | +1.92% |
| CAP/USDT:USDT | below_1h_threshold | +1.88% | +1.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
