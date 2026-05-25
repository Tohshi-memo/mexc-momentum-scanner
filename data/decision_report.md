# Decision Report

- generated_at: 2026-05-25T01:49:42.141934+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4838**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4838, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.12% | **+0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.25% | **+0.25%** |
| MARKET | 20/20 | 100.0% | +0.12% | **+0.12%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.03% | **+0.02%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.33% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.34% | **+0.94%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.87% | **+0.52%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.65% | **+0.36%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.38% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.01** / 初期 $100.00 (+23.01%)
- 確定: 644件 (Win 159 / Loss 205 / Flat 280) / skip 755件
- 成長率目線: 平均log +0.000322 / 幾何平均 +0.032% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $123.01

## 4. Latest Market Context

- 更新: 2026-05-25T01:49:39.815056+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=77081.2
- Funnel: target 764 → liquid 112 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SPORTFUN/USDT:USDT | +14.08% | $1,081,755.54 |
| EDU/USDT:USDT | +5.66% | $1,034,364.92 |
| AGT/USDT:USDT | +5.52% | $7,304,086.04 |
| SUPER/USDT:USDT | +5.08% | $3,563,594.72 |
| NIL/USDT:USDT | +3.94% | $13,633,421.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +3.18% | +3.23% |
| AGT/USDT:USDT | below_1h_threshold | +2.23% | +2.28% |
| MYX/USDT:USDT | below_1h_threshold | +1.79% | +1.84% |
| RAVE/USDT:USDT | below_1h_threshold | +1.58% | +1.63% |
| PHA/USDT:USDT | below_1h_threshold | +0.92% | +0.97% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
