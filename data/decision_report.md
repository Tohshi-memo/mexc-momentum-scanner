# Decision Report

- generated_at: 2026-06-10T20:55:25.053133+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6265**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6265, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.01% | **-1.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.24% | **+0.13%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_8PCT | 5/20 | 25.0% | -0.06% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.41% | **+1.41%** |
| ASK_LONG | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.38% | **+0.96%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.35% | **+0.61%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$152.74** / 初期 $100.00 (+52.74%)
- 確定: 1251件 (Win 314 / Loss 388 / Flat 549) / skip 1575件
- 成長率目線: 平均log +0.000339 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $152.74

## 4. Latest Market Context

- 更新: 2026-06-10T20:55:18.482349+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=61738.0
- Funnel: target 785 → liquid 155 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.2 >= 65=1, 4h RSI 80.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +70.55% | $28,405,439.73 |
| BEAT/USDT:USDT | +30.01% | $148,323,385.37 |
| JCT/USDT:USDT | +14.79% | $2,324,359.43 |
| SKYAI/USDT:USDT | +11.60% | $5,628,117.71 |
| STRAX/USDT:USDT | +6.16% | $1,217,478.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +4.75% | +5.03% |
| LAB/USDT:USDT | below_1h_threshold | +3.66% | +3.94% |
| STRAX/USDT:USDT | below_1h_threshold | +3.59% | +3.87% |
| AGT/USDT:USDT | below_1h_threshold | +2.58% | +2.86% |
| H/USDT:USDT | below_1h_threshold | +2.37% | +2.65% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
