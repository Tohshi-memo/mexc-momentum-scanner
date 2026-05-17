# Decision Report

- generated_at: 2026-05-17T12:58:32.304283+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4400**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4400, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.19% | **-0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.86% | **+0.57%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.38% | **+0.30%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.41% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.92% | **+1.44%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.48% | **+1.03%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.02% | **+1.02%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.02% | **+0.86%** |
| ASK_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$118.38** / 初期 $100.00 (+18.38%)
- 確定: 398件 (Win 102 / Loss 137 / Flat 159) / skip 563件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $118.38

## 4. Latest Market Context

- 更新: 2026-05-17T12:58:30.090706+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=78302.0
- Funnel: target 760 → liquid 118 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +49.56% | $12,314,114.39 |
| AIA/USDT:USDT | +31.38% | $15,058,078.19 |
| CGPT/USDT:USDT | +18.47% | $2,442,118.21 |
| KAIA/USDT:USDT | +15.74% | $2,282,249.43 |
| ASTEROID/USDT:USDT | +14.20% | $4,545,436.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.15% | +3.24% |
| UP/USDT:USDT | below_1h_threshold | +2.23% | +2.31% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.18% | +2.27% |
| RIVER/USDT:USDT | below_1h_threshold | +1.88% | +1.97% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.85% | +1.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
