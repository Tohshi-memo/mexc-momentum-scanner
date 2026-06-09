# Decision Report

- generated_at: 2026-06-09T08:30:22.852335+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6123**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6123, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.07% | **-1.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.52% | **+1.52%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.46% | **+1.36%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.30% | **+1.16%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.99% | **+1.09%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.65% | **+1.07%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$154.22** / 初期 $100.00 (+54.22%)
- 確定: 1163件 (Win 291 / Loss 358 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000373 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SLX/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $154.22

## 4. Latest Market Context

- 更新: 2026-06-09T08:30:20.032732+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.57% price=62812.7
- Funnel: target 774 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +57.49% | $22,645,630.19 |
| SLX/USDT:USDT | +38.68% | $3,235,468.02 |
| POWER/USDT:USDT | +15.13% | $1,881,180.80 |
| FOLKS/USDT:USDT | +13.25% | $1,703,780.49 |
| LIGHT/USDT:USDT | +11.29% | $1,107,451.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FOLKS/USDT:USDT | below_1h_threshold | +4.98% | +5.55% |
| ZEST/USDT:USDT | below_1h_threshold | +4.54% | +5.10% |
| CTR/USDT:USDT | below_1h_threshold | +2.05% | +2.62% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.62% | +2.18% |
| POWER/USDT:USDT | below_1h_threshold | +1.44% | +2.00% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
