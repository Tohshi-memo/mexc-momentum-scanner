# Decision Report

- generated_at: 2026-06-02T06:13:48.414173+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5413**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5413, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +2.24% | **+0.34%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |
| ASK | 20/20 | 100.0% | -0.35% | **-0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.70% | **+2.02%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.03% | **+1.83%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.00% | **+1.10%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.51% | **+0.83%** |

## 2. $100 Live Portfolio

- 残高: **$96.63** / 初期 $100.00 (-3.37%)
- 確定トレード: 84件 (TP 24 / SL 57 / EXP 3)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.63
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$135.47** / 初期 $100.00 (+35.47%)
- 確定: 925件 (Win 217 / Loss 274 / Flat 434) / skip 1049件
- 成長率目線: 平均log +0.000328 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $135.47

## 4. Latest Market Context

- 更新: 2026-06-02T06:13:45.726023+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=70232.1
- Funnel: target 777 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +57.12% | $8,914,347.16 |
| ESPORTS/USDT:USDT | +26.42% | $11,911,834.04 |
| US/USDT:USDT | +25.79% | $1,051,983.02 |
| H/USDT:USDT | +23.14% | $56,447,950.93 |
| LAB/USDT:USDT | +19.95% | $216,104,982.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.72% | +3.73% |
| MYX/USDT:USDT | below_1h_threshold | +3.18% | +3.18% |
| EPIC/USDT:USDT | below_1h_threshold | +3.18% | +3.18% |
| BSB/USDT:USDT | below_1h_threshold | +3.15% | +3.15% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.92% | +1.92% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
