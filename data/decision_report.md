# Decision Report

- generated_at: 2026-06-05T11:09:19.010904+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5716**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.58% / filled 20/20。**
- 全期間 MARKET基準: n=5716, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.54% | **+1.31%** |
| ASK | 20/20 | 100.0% | +1.28% | **+1.28%** |
| LIMIT_3PCT | 16/20 | 80.0% | +1.26% | **+1.01%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.84% | **+0.64%** |
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.78% | **+1.33%** |
| LIMIT_BB3S_LONG | 2/7 | 28.6% | +3.58% | **+1.02%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.03% | **+1.01%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.96% | **+0.63%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.67% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1010件 (Win 239 / Loss 313 / Flat 458) / skip 1267件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-05T11:09:16.085039+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=62318.1
- Funnel: target 773 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +79.08% | $24,022,439.24 |
| BABY/USDT:USDT | +65.23% | $6,676,171.14 |
| CLO/USDT:USDT | +18.55% | $1,118,138.15 |
| BEAT/USDT:USDT | +11.49% | $28,032,578.25 |
| AAOISTOCK/USDT:USDT | +10.27% | $2,290,618.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OPN/USDT:USDT | below_1h_threshold | +1.84% | +2.16% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.75% | +1.07% |
| EPIC/USDT:USDT | below_1h_threshold | +0.50% | +0.81% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +0.42% | +0.74% |
| XOMSTOCK/USDT:USDT | below_1h_threshold | +0.28% | +0.59% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
