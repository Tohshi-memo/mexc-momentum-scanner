# Decision Report

- generated_at: 2026-06-18T00:19:46.718437+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6982**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6982, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.15% | **-1.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.35% | **+0.54%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.06% | **+0.04%** |
| LIMIT_2PCT | 18/20 | 90.0% | -0.10% | **-0.09%** |
| LIMIT_10PCT | 6/20 | 30.0% | -0.85% | **-0.25%** |
| LIMIT_8PCT | 7/20 | 35.0% | -1.80% | **-0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.64% | **+2.64%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.87% | **+0.93%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.66% | **+0.75%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.11% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$204.72** / 初期 $100.00 (+104.72%)
- 確定: 1829件 (Win 502 / Loss 576 / Flat 751) / skip 1714件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $204.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$103.75** / 初期 $100.00 (+3.75%)
- 確定: 255件 (Win 68 / Loss 65 / Flat 122) / skip 138件
- 成長率目線: 平均log +0.000144 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0766 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $103.75

## 5. Latest Market Context

- 更新: 2026-06-18T00:19:40.616881+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=64626.8
- Funnel: target 790 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +115.29% | $22,634,388.26 |
| O/USDT:USDT | +77.39% | $1,467,343.36 |
| SYN/USDT:USDT | +41.48% | $4,233,799.73 |
| H/USDT:USDT | +15.28% | $38,070,406.63 |
| RE/USDT:USDT | +14.57% | $1,852,468.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.85% | +4.62% |
| ID/USDT:USDT | below_1h_threshold | +3.77% | +3.54% |
| US/USDT:USDT | below_1h_threshold | +3.58% | +3.35% |
| STG/USDT:USDT | below_1h_threshold | +3.05% | +2.82% |
| BEAT/USDT:USDT | below_1h_threshold | +3.01% | +2.78% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
