# Decision Report

- generated_at: 2026-06-12T08:48:48.011406+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6489**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.46% / filled 20/20。**
- 全期間 MARKET基準: n=6489, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/20 | 20.0% | +4.69% | **+0.94%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.57% | **+0.51%** |
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.31% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| ASK_LONG | 20/20 | 100.0% | +0.33% | **+0.33%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.65% | **+0.29%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.27% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$95.17** / 初期 $100.00 (-4.83%)
- 確定トレード: 17件 (TP 2 / SL 14 / EXP 1)
- 最新: ZBT/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$161.50** / 初期 $100.00 (+61.50%)
- 確定: 1363件 (Win 368 / Loss 439 / Flat 556) / skip 1687件
- 成長率目線: 平均log +0.000352 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPACE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $161.50

## 4. Latest Market Context

- 更新: 2026-06-12T08:48:44.627387+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.53% price=63400.0
- Funnel: target 779 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +106.44% | $148,870,989.55 |
| ESPORTS/USDT:USDT | +49.86% | $37,509,023.74 |
| NAORIS/USDT:USDT | +42.19% | $2,884,402.95 |
| XPL/USDT:USDT | +37.39% | $9,349,240.44 |
| H/USDT:USDT | +26.20% | $44,976,965.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HMSTR/USDT:USDT | below_1h_threshold | +4.30% | +3.78% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +3.94% | +3.42% |
| ZEC/USDT:USDT | below_1h_threshold | +2.24% | +1.71% |
| COAI/USDT:USDT | below_1h_threshold | +2.03% | +1.51% |
| NEAR/USDT:USDT | below_1h_threshold | +1.96% | +1.43% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
