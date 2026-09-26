# Decision Report

- generated_at: 2026-09-26T00:46:38.955261+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15557**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15557, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.88% | **+0.83%** |
| LIMIT_BB3S | 3/18 | 16.7% | +3.32% | **+0.55%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.95% | **+0.52%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.77% | **+0.46%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +4.11% | **+1.44%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.09% | **+0.82%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.77% | **+0.73%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.04% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$120.79** / 初期 $100.00 (+20.79%)
- 確定トレード: 223件 (TP 82 / SL 135 / EXP 6)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.79
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,201.55** / 初期 $100.00 (+1101.55%)
- 確定: 5920件 (Win 1745 / Loss 1898 / Flat 2277) / skip 6198件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,201.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.14** / 初期 $100.00 (+156.14%)
- 確定: 3489件 (Win 956 / Loss 794 / Flat 1739) / skip 5479件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0231 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $256.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.07** / 初期 $100.00 (+19.07%)
- 確定: 3183件 (Win 935 / Loss 1262 / Flat 986) / pending 3件 / skip 3843件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000237 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $119.07

## 6. Latest Market Context

- 更新: 2026-09-26T00:46:24.192807+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=83849.9
- Funnel: target 1067 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +47.00% | $1,276,872.63 |
| BR/USDT:USDT | +19.13% | $9,421,832.59 |
| PHA/USDT:USDT | +15.88% | $25,925,917.35 |
| SEI/USDT:USDT | +11.91% | $38,166,990.59 |
| ONE/USDT:USDT | +11.12% | $8,191,538.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +2.85% | +3.10% |
| AXS/USDT:USDT | below_1h_threshold | +2.80% | +3.05% |
| LYN/USDT:USDT | below_1h_threshold | +2.54% | +2.79% |
| BTW/USDT:USDT | below_1h_threshold | +1.57% | +1.82% |
| MUBARAK/USDT:USDT | below_1h_threshold | +1.39% | +1.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
