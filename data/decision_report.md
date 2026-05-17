# Decision Report

- generated_at: 2026-05-17T06:38:32.705165+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4388**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4388, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.03% | **+0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.57% | **+0.51%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.78% | **+0.31%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.36% | **+0.25%** |
| MARKET | 20/20 | 100.0% | +0.03% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.17% | **+0.76%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.35% | **+0.27%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.39% | **+0.25%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.31% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.68** / 初期 $100.00 (+17.68%)
- 確定: 393件 (Win 97 / Loss 137 / Flat 159) / skip 556件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CGPT/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account -0.27% 残高後 $117.68

## 4. Latest Market Context

- 更新: 2026-05-17T06:38:28.774441+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=78074.0
- Funnel: target 760 → liquid 126 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +38.32% | $8,431,582.01 |
| CGPT/USDT:USDT | +26.00% | $1,867,559.73 |
| BSB/USDT:USDT | +19.96% | $4,694,252.39 |
| ASTEROID/USDT:USDT | +18.52% | $4,300,459.83 |
| AIGENSYN/USDT:USDT | +11.36% | $2,775,269.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UP/USDT:USDT | below_1h_threshold | +3.95% | +3.97% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.41% | +2.43% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.03% | +2.04% |
| BSB/USDT:USDT | below_1h_threshold | +1.96% | +1.98% |
| LAB/USDT:USDT | below_1h_threshold | +1.65% | +1.67% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
