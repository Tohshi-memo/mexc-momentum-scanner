# Decision Report

- generated_at: 2026-05-20T17:04:35.208188+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4560**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4560, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.28% | **-1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.15% | **+0.46%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.12% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.24% | **+1.24%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.83% | **+1.13%** |
| ASK_LONG | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.99% | **+0.60%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +1.22% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.58** / 初期 $100.00 (+25.58%)
- 確定: 522件 (Win 137 / Loss 176 / Flat 209) / skip 599件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $125.58

## 4. Latest Market Context

- 更新: 2026-05-20T17:04:33.219264+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=77261.0
- Funnel: target 763 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +19.63% | $37,238,612.32 |
| EDEN/USDT:USDT | +15.14% | $27,958,944.33 |
| SAHARA/USDT:USDT | +4.36% | $1,144,615.00 |
| WLD/USDT:USDT | +3.78% | $19,813,256.34 |
| PENDLE/USDT:USDT | +3.42% | $1,761,737.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +1.54% | +1.60% |
| WLD/USDT:USDT | below_1h_threshold | +0.87% | +0.92% |
| NAORIS/USDT:USDT | below_1h_threshold | +0.79% | +0.84% |
| BSB/USDT:USDT | below_1h_threshold | +0.75% | +0.80% |
| FIDA/USDT:USDT | below_1h_threshold | +0.63% | +0.68% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
