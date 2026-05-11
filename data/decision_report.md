# Decision Report

- generated_at: 2026-05-11T19:13:13.970890+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4065**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4065, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.47% | **-0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.52% | **+1.29%** |
| ASK_LONG | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.30% | **+0.84%** |
| MARKET_LONG | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 408件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T19:13:07.996746+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=81904.3
- Funnel: target 757 → liquid 190 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +25.91% | $130,694,134.32 |
| USELESS/USDT:USDT | +18.04% | $1,767,334.43 |
| SKYAI/USDT:USDT | +14.31% | $32,674,861.83 |
| ASTEROID/USDT:USDT | +12.23% | $2,657,536.86 |
| B/USDT:USDT | +11.85% | $31,503,133.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +2.34% | +2.24% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.65% | +1.54% |
| USELESS/USDT:USDT | below_1h_threshold | +1.62% | +1.52% |
| BRETT/USDT:USDT | below_1h_threshold | +1.24% | +1.14% |
| RUNE/USDT:USDT | below_1h_threshold | +1.24% | +1.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
