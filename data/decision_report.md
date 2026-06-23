# Decision Report

- generated_at: 2026-06-23T15:02:01.456934+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7428**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7428, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.00% | **+0.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/19 | 26.3% | +2.87% | **+0.75%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.21% | **+0.12%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.87% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +3.64% | **+1.09%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.20% | **+0.84%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.08% | **+0.59%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.66% | **+0.53%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$101.94** / 初期 $100.00 (+1.94%)
- 確定トレード: 29件 (TP 11 / SL 18 / EXP 0)
- 最新: RE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$228.71** / 初期 $100.00 (+128.71%)
- 確定: 2081件 (Win 617 / Loss 690 / Flat 774) / skip 1908件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $228.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.73** / 初期 $100.00 (+6.73%)
- 確定: 319件 (Win 92 / Loss 87 / Flat 140) / skip 520件
- 成長率目線: 平均log +0.000204 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0248 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $106.73

## 5. Latest Market Context

- 更新: 2026-06-23T15:01:56.896972+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=62418.7
- Funnel: target 802 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +33.48% | $3,807,988.49 |
| ARX/USDT:USDT | +29.72% | $17,998,628.57 |
| BR/USDT:USDT | +21.54% | $2,136,755.35 |
| LIGHT/USDT:USDT | +18.04% | $1,098,776.12 |
| RESOLV/USDT:USDT | +15.06% | $10,199,077.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RESOLV/USDT:USDT | below_1h_threshold | +1.76% | +1.83% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.95% | +1.02% |
| BEAT/USDT:USDT | below_1h_threshold | +0.87% | +0.94% |
| POPCAT/USDT:USDT | below_1h_threshold | +0.64% | +0.71% |
| ARX/USDT:USDT | below_1h_threshold | +0.56% | +0.63% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
