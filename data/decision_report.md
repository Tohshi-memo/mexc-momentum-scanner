# Decision Report

- generated_at: 2026-06-01T22:28:01.798263+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5370**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5370, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.47% | **-0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.44% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.18% | **+0.98%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.57% | **+0.86%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.59% | **+0.71%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 83件 (TP 24 / SL 56 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 1037件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T22:27:59.134038+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=71276.1
- Funnel: target 772 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +29.52% | $6,458,082.47 |
| PLAY/USDT:USDT | +15.28% | $7,405,067.58 |
| H/USDT:USDT | +14.08% | $62,915,562.67 |
| UB/USDT:USDT | +13.70% | $2,206,511.93 |
| WLD/USDT:USDT | +12.93% | $134,525,263.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VIC/USDT:USDT | below_1h_threshold | +4.92% | +4.54% |
| H/USDT:USDT | below_1h_threshold | +4.51% | +4.14% |
| LAB/USDT:USDT | below_1h_threshold | +4.44% | +4.06% |
| BILL/USDT:USDT | below_1h_threshold | +3.51% | +3.13% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.23% | +2.85% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
