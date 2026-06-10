# Decision Report

- generated_at: 2026-06-10T01:07:48.064574+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6172**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6172, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.95% | **+0.50%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.54% | **+0.32%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.05% | **+0.53%** |
| ASK_LONG | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$147.27** / 初期 $100.00 (+47.27%)
- 確定: 1190件 (Win 297 / Loss 375 / Flat 518) / skip 1543件
- 成長率目線: 平均log +0.000325 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_5PCT_LONG` EXPIRED account +0.00% 残高後 $147.27

## 4. Latest Market Context

- 更新: 2026-06-10T01:07:45.611853+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=61752.7
- Funnel: target 778 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +52.83% | $12,154,264.32 |
| STG/USDT:USDT | +27.43% | $3,074,813.58 |
| HOME/USDT:USDT | +14.44% | $4,408,391.70 |
| UB/USDT:USDT | +12.87% | $1,391,192.27 |
| SENT/USDT:USDT | +9.00% | $1,630,980.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.39% | +4.61% |
| STG/USDT:USDT | below_1h_threshold | +1.72% | +1.94% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.07% | +1.28% |
| LIT/USDT:USDT | below_1h_threshold | +1.02% | +1.24% |
| IO/USDT:USDT | below_1h_threshold | +0.68% | +0.89% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
