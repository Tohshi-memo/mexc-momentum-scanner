# Decision Report

- generated_at: 2026-07-06T03:52:40.028392+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8368**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.53% / filled 20/20。**
- 全期間 MARKET基準: n=8368, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.53% | **+1.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.74% | **+1.74%** |
| MARKET | 20/20 | 100.0% | +1.53% | **+1.53%** |
| LIMIT_1PCT | 14/20 | 70.0% | +1.49% | **+1.04%** |
| LIMIT_4PCT | 9/20 | 45.0% | +2.22% | **+1.00%** |
| LIMIT_3PCT | 9/20 | 45.0% | +1.68% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.54% | **+0.85%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.78% | **+0.80%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.79% | **+0.51%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.81% | **+0.40%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$102.08** / 初期 $100.00 (+2.08%)
- 確定トレード: 66件 (TP 23 / SL 42 / EXP 1)
- 最新: EPIC/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.08
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$318.73** / 初期 $100.00 (+218.73%)
- 確定: 2622件 (Win 832 / Loss 886 / Flat 904) / skip 2307件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $318.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 639件 (Win 152 / Loss 158 / Flat 329) / skip 1140件
- 成長率目線: 平均log +0.000084 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASED/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.26% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-06T03:37:48.794946+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=63255.6
- Funnel: target 836 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEROC0MPUTE/USDT:USDT | +15.96% | $1,602,920.86 |
| TRB/USDT:USDT | +15.42% | $7,853,997.41 |
| LIT/USDT:USDT | +9.16% | $12,129,595.11 |
| UB/USDT:USDT | +8.49% | $1,340,157.16 |
| GIGGLE/USDT:USDT | +6.87% | $1,709,089.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DYDX/USDT:USDT | below_1h_threshold | +2.90% | +3.17% |
| XPL/USDT:USDT | below_1h_threshold | +2.14% | +2.40% |
| RESOLV/USDT:USDT | below_1h_threshold | +2.00% | +2.27% |
| BASED/USDT:USDT | below_1h_threshold | +1.82% | +2.09% |
| GIGGLE/USDT:USDT | below_1h_threshold | +1.64% | +1.91% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
