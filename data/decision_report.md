# Decision Report

- generated_at: 2026-05-19T16:23:50.490154+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4479**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4479, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.07% | **+0.04%** |
| ASK | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +4.07% | **+3.26%** |
| MARKET_LONG | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.15% | **+0.75%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.11% | **+0.72%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.94% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定: 473件 (Win 124 / Loss 164 / Flat 185) / skip 567件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $121.49

## 4. Latest Market Context

- 更新: 2026-05-19T16:23:45.175414+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=76501.5
- Funnel: target 764 → liquid 134 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.5 >= 65=1, 4h RSI 70.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +17.16% | $7,474,933.59 |
| LAB/USDT:USDT | +8.12% | $81,608,804.33 |
| EDEN/USDT:USDT | +5.67% | $3,997,477.48 |
| VVV/USDT:USDT | +3.14% | $5,794,656.23 |
| AT/USDT:USDT | +2.60% | $2,726,854.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +3.18% | +3.16% |
| AT/USDT:USDT | below_1h_threshold | +2.61% | +2.59% |
| AIA/USDT:USDT | below_1h_threshold | +1.90% | +1.89% |
| GUA/USDT:USDT | below_1h_threshold | +1.80% | +1.78% |
| LIT/USDT:USDT | below_1h_threshold | +1.65% | +1.63% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
