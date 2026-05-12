# Decision Report

- generated_at: 2026-05-12T08:33:19.555390+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4101**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4101, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.18% | **-1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +3.23% | **+0.48%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |
| LIMIT_ATR | 17/20 | 85.0% | -0.59% | **-0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.43% | **+1.82%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.81% | **+1.55%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.90% | **+1.24%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.24% | **+1.12%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.04% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$111.77** / 初期 $100.00 (+11.77%)
- 確定: 237件 (Win 62 / Loss 82 / Flat 93) / skip 425件
- 成長率目線: 平均log +0.000469 / 幾何平均 +0.047% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VVV/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $111.77

## 4. Latest Market Context

- 更新: 2026-05-12T08:33:13.714537+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=80833.1
- Funnel: target 761 → liquid 190 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +41.40% | $3,530,710.38 |
| SAGA/USDT:USDT | +40.97% | $11,155,764.76 |
| SKYAI/USDT:USDT | +36.05% | $43,458,415.97 |
| USELESS/USDT:USDT | +31.91% | $6,370,345.73 |
| GUA/USDT:USDT | +31.86% | $2,413,715.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +3.95% | +3.92% |
| SAHARA/USDT:USDT | below_1h_threshold | +3.35% | +3.32% |
| H/USDT:USDT | below_1h_threshold | +2.77% | +2.75% |
| BILL/USDT:USDT | below_1h_threshold | +2.56% | +2.53% |
| GUA/USDT:USDT | below_1h_threshold | +2.46% | +2.44% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
