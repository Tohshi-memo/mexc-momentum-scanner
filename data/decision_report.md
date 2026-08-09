# Decision Report

- generated_at: 2026-08-09T13:51:29.606555+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11030**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.38% / filled 20/20。**
- 全期間 MARKET基準: n=11030, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.38% | **+2.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.38% | **+2.38%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.57% | **+1.18%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.28% | **+0.80%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.31% | **+0.72%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.80% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.04% | **+0.51%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.70% | **+0.51%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.15% | **+0.22%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -0.22% | **-0.13%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$628.11** / 初期 $100.00 (+528.11%)
- 確定: 3931件 (Win 1230 / Loss 1281 / Flat 1420) / skip 3660件
- 成長率目線: 平均log +0.000467 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XAI/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $628.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1512件 (Win 424 / Loss 360 / Flat 728) / skip 2929件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0137 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.64** / 初期 $100.00 (+17.64%)
- 確定: 1264件 (Win 391 / Loss 481 / Flat 392) / pending 5件 / skip 1236件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000317 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COOKIE/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $117.64

## 6. Latest Market Context

- 更新: 2026-08-09T13:51:17.256070+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=65174.9
- Funnel: target 961 → liquid 152 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +113.47% | $72,062,248.81 |
| BMT/USDT:USDT | +79.35% | $5,888,501.16 |
| COOKIE/USDT:USDT | +31.93% | $6,404,349.61 |
| MUBARAK/USDT:USDT | +28.10% | $3,186,174.25 |
| BEAT/USDT:USDT | +22.52% | $69,686,914.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PUMPFUN/USDT:USDT | below_1h_threshold | +3.51% | +3.12% |
| INX/USDT:USDT | below_1h_threshold | +1.93% | +1.54% |
| IOTX/USDT:USDT | below_1h_threshold | +1.50% | +1.12% |
| WLD/USDT:USDT | below_1h_threshold | +1.49% | +1.11% |
| BLUAI/USDT:USDT | below_1h_threshold | +1.03% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
