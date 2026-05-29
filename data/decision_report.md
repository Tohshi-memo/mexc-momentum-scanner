# Decision Report

- generated_at: 2026-05-29T15:45:13.522565+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5056**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5056, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.02% | **+0.92%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.85% | **+0.81%** |
| LIMIT_BB3S | 7/12 | 58.3% | +1.05% | **+0.61%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.48% | **+0.37%** |
| ASK | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.46% | **+1.38%** |
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +1.90% | **+0.95%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +2.29% | **+0.46%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.28% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$98.60** / 初期 $100.00 (-1.40%)
- 確定トレード: 74件 (TP 22 / SL 49 / EXP 3)
- 最新: LIT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 877件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T15:45:11.055723+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.95% price=73759.6
- Funnel: target 777 → liquid 153 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=3, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +147.77% | $126,025,162.70 |
| HEI/USDT:USDT | +96.27% | $3,991,543.89 |
| ID/USDT:USDT | +44.02% | $3,221,810.80 |
| LAB/USDT:USDT | +25.99% | $95,909,994.65 |
| DELLSTOCK/USDT:USDT | +25.80% | $11,157,285.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_relative_strength | +5.73% | +4.78% |
| USELESS/USDT:USDT | below_relative_strength | +5.45% | +4.50% |
| INJ/USDT:USDT | below_relative_strength | +5.13% | +4.18% |
| DYDX/USDT:USDT | below_1h_threshold | +4.71% | +3.76% |
| ZBCN/USDT:USDT | below_1h_threshold | +4.42% | +3.47% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
