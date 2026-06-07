# Decision Report

- generated_at: 2026-06-07T19:51:03.372829+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5996**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.24% / filled 20/20。**
- 全期間 MARKET基準: n=5996, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.52% | **+0.52%** |
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.69% | **+5.69%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.27% | **+1.02%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.91% | **+0.69%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.27** / 初期 $100.00 (+49.27%)
- 確定: 1113件 (Win 269 / Loss 336 / Flat 508) / skip 1444件
- 成長率目線: 平均log +0.000360 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $149.27

## 4. Latest Market Context

- 更新: 2026-06-07T19:50:59.986120+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.12% price=61303.3
- Funnel: target 768 → liquid 129 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.2 >= 65=1, 4h RSI 83.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +20.43% | $3,280,050.62 |
| EPIC/USDT:USDT | +13.40% | $1,175,787.21 |
| BEAT/USDT:USDT | +11.98% | $55,972,438.05 |
| VELVET/USDT:USDT | +11.47% | $2,922,501.66 |
| BTW/USDT:USDT | +8.56% | $14,600,563.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.83% | +5.95% |
| VELVET/USDT:USDT | below_1h_threshold | +4.58% | +5.70% |
| BEAT/USDT:USDT | below_1h_threshold | +3.74% | +4.86% |
| ALLO/USDT:USDT | below_1h_threshold | +1.54% | +2.66% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.24% | +2.36% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
