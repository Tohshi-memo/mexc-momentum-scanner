# Decision Report

- generated_at: 2026-06-02T20:31:49.107847+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5487**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5487, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.13% | **-2.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.16% | **+0.58%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.66% | **+0.55%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +3.31% | **+3.31%** |
| MARKET_LONG | 20/20 | 100.0% | +3.13% | **+3.13%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +3.48% | **+2.32%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +3.30% | **+2.14%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +3.43% | **+1.71%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 976件 (Win 229 / Loss 300 / Flat 447) / skip 1072件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-02T20:31:46.313890+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=67117.7
- Funnel: target 770 → liquid 154 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.5 >= 65=1, 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +28.21% | $13,037,727.20 |
| LAB/USDT:USDT | +19.20% | $183,082,854.94 |
| ESPORTS/USDT:USDT | +17.02% | $9,548,970.08 |
| LIT/USDT:USDT | +15.93% | $5,569,262.88 |
| PANWSTOCK/USDT:USDT | +11.43% | $3,371,148.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EPIC/USDT:USDT | below_1h_threshold | +5.00% | +5.24% |
| LAB/USDT:USDT | below_1h_threshold | +3.67% | +3.92% |
| BSB/USDT:USDT | below_1h_threshold | +3.04% | +3.29% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.84% | +3.08% |
| EDGE/USDT:USDT | below_1h_threshold | +2.81% | +3.05% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
