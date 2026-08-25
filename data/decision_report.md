# Decision Report

- generated_at: 2026-08-25T00:41:35.608699+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12556**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12556, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.83% | **-0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.41% | **+0.72%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.73% | **+0.51%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +3.50% | **+2.45%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.99% | **+2.09%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.81% | **+1.69%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.78% | **+1.39%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.58% | **+1.26%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$694.71** / 初期 $100.00 (+594.71%)
- 確定: 4536件 (Win 1383 / Loss 1488 / Flat 1665) / skip 4581件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $694.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.16** / 初期 $100.00 (+56.16%)
- 確定: 1973件 (Win 536 / Loss 471 / Flat 966) / skip 3994件
- 成長率目線: 平均log +0.000226 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0589 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $156.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.37** / 初期 $100.00 (+15.37%)
- 確定: 1913件 (Win 561 / Loss 728 / Flat 624) / pending 0件 / skip 2116件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000171 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.37

## 6. Latest Market Context

- 更新: 2026-08-25T00:41:22.183212+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=78910.1
- Funnel: target 1022 → liquid 184 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +89.45% | $3,620,223.08 |
| TAC/USDT:USDT | +28.72% | $1,179,791.80 |
| CASHCAT/USDT:USDT | +19.61% | $2,516,587.58 |
| ONG/USDT:USDT | +19.49% | $2,999,703.04 |
| STORJ/USDT:USDT | +18.15% | $5,240,945.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JUP/USDT:USDT | below_1h_threshold | +3.42% | +3.47% |
| SOL/USDT:USDT | below_1h_threshold | +2.12% | +2.18% |
| RE/USDT:USDT | below_1h_threshold | +2.02% | +2.08% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.65% | +1.70% |
| PONS/USDT:USDT | below_1h_threshold | +1.50% | +1.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
