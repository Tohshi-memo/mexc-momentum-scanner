# Decision Report

- generated_at: 2026-06-10T08:29:28.214189+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6203**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6203, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.55% | **-1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.31% | **+0.14%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.95% | **+1.95%** |
| ASK_LONG | 20/20 | 100.0% | +1.28% | **+1.28%** |
| LIMIT_ATR_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +0.77% | **+0.46%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +0.92% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.27** / 初期 $100.00 (+51.27%)
- 確定: 1219件 (Win 303 / Loss 378 / Flat 538) / skip 1545件
- 成長率目線: 平均log +0.000340 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $151.27

## 4. Latest Market Context

- 更新: 2026-06-10T08:29:25.629290+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=61474.9
- Funnel: target 785 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +48.54% | $8,538,106.22 |
| BTW/USDT:USDT | +26.61% | $30,086,083.29 |
| KAT/USDT:USDT | +23.10% | $1,003,289.94 |
| ESPORTS/USDT:USDT | +22.19% | $24,856,673.30 |
| UB/USDT:USDT | +19.74% | $2,180,447.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.05% | +4.34% |
| BLESS/USDT:USDT | below_1h_threshold | +3.84% | +4.13% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.45% | +2.74% |
| UB/USDT:USDT | below_1h_threshold | +1.81% | +2.10% |
| RUNE/USDT:USDT | below_1h_threshold | +1.59% | +1.88% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
