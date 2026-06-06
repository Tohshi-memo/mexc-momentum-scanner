# Decision Report

- generated_at: 2026-06-06T16:39:01.122216+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5867**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5867, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.02% | **+0.36%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| ASK | 20/20 | 100.0% | +0.18% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.25% | **+1.46%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.71% | **+0.81%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.60% | **+0.64%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1014件 (Win 239 / Loss 313 / Flat 462) / skip 1414件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T16:38:55.523313+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=60532.2
- Funnel: target 771 → liquid 141 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +7.76% | $6,819,737.19 |
| PORTAL/USDT:USDT | +7.23% | $2,584,590.42 |
| HOME/USDT:USDT | +4.26% | $10,431,295.36 |
| BTW/USDT:USDT | +3.50% | $20,545,131.12 |
| BEAT/USDT:USDT | +3.44% | $34,660,663.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +4.72% | +5.09% |
| BTW/USDT:USDT | below_1h_threshold | +3.51% | +3.87% |
| BEAT/USDT:USDT | below_1h_threshold | +3.45% | +3.82% |
| SLX/USDT:USDT | below_1h_threshold | +2.89% | +3.25% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.54% | +2.91% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
