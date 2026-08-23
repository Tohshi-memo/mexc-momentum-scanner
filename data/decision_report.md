# Decision Report

- generated_at: 2026-08-23T14:06:27.460383+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12456**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12456, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.88% | **-0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +0.92% | **+0.69%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +1.06% | **+0.63%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.32% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.37% | **+2.37%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.61% | **+1.57%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.30% | **+1.49%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.57% | **+1.10%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.44% | **+0.86%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$704.15** / 初期 $100.00 (+604.15%)
- 確定: 4483件 (Win 1370 / Loss 1469 / Flat 1644) / skip 4534件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_4PCT_LONG` TP_HIT account +1.00% 残高後 $704.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.61** / 初期 $100.00 (+57.61%)
- 確定: 1936件 (Win 534 / Loss 465 / Flat 937) / skip 3931件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0050 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PROM/USDT:USDT `LIMIT_FIB1272` TP_HIT account +0.69% 残高後 $157.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.63** / 初期 $100.00 (+16.63%)
- 確定: 1864件 (Win 549 / Loss 707 / Flat 608) / pending 1件 / skip 2065件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000072 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.63

## 6. Latest Market Context

- 更新: 2026-08-23T14:06:17.008168+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=77462.2
- Funnel: target 1018 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +46.47% | $68,612,857.14 |
| UAI/USDT:USDT | +30.40% | $6,042,833.38 |
| ZRO/USDT:USDT | +24.10% | $24,532,296.87 |
| STX/USDT:USDT | +22.75% | $13,411,122.46 |
| PENDLE/USDT:USDT | +19.02% | $3,476,084.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PROM/USDT:USDT | below_1h_threshold | +3.69% | +3.71% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.78% | +2.79% |
| ZAMA/USDT:USDT | below_1h_threshold | +1.75% | +1.76% |
| STX/USDT:USDT | below_1h_threshold | +1.48% | +1.49% |
| ZRO/USDT:USDT | below_1h_threshold | +1.42% | +1.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
