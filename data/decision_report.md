# Decision Report

- generated_at: 2026-06-02T08:25:55.470390+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5428**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5428, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 11/18 | 61.1% | +0.90% | **+0.55%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.67% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.77% | **+1.33%** |
| ASK_LONG | 20/20 | 100.0% | +0.83% | **+0.83%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.43% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$96.14** / 初期 $100.00 (-3.86%)
- 確定トレード: 85件 (TP 24 / SL 58 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.14
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.95** / 初期 $100.00 (+33.95%)
- 確定: 940件 (Win 221 / Loss 282 / Flat 437) / skip 1049件
- 成長率目線: 平均log +0.000311 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $133.95

## 4. Latest Market Context

- 更新: 2026-06-02T08:25:52.057206+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=69866.1
- Funnel: target 772 → liquid 150 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.6 >= 65=1, 4h RSI 65.7 >= 65=1, 4h RSI 81.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +43.65% | $16,955,810.13 |
| US/USDT:USDT | +40.13% | $1,953,153.94 |
| ESPORTS/USDT:USDT | +34.04% | $12,320,239.12 |
| MRVLSTOCK/USDT:USDT | +24.12% | $3,066,619.54 |
| H/USDT:USDT | +22.88% | $58,627,215.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +3.16% | +3.46% |
| JTO/USDT:USDT | below_1h_threshold | +2.59% | +2.89% |
| AVGOSTOCK/USDT:USDT | below_1h_threshold | +1.52% | +1.83% |
| MERL/USDT:USDT | below_1h_threshold | +1.39% | +1.69% |
| EPIC/USDT:USDT | below_1h_threshold | +1.21% | +1.52% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
