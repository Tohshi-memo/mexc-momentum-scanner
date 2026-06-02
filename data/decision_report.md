# Decision Report

- generated_at: 2026-06-02T00:58:57.797536+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5385**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.18% / filled 20/20。**
- 全期間 MARKET基準: n=5385, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.18% | **+2.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.80% | **+2.80%** |
| MARKET | 20/20 | 100.0% | +2.18% | **+2.18%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.22% | **+1.11%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.03% | **+0.67%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.85% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.09% | **-0.05%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.52% | **-0.10%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 83件 (TP 24 / SL 56 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$132.51** / 初期 $100.00 (+32.51%)
- 確定: 900件 (Win 209 / Loss 270 / Flat 421) / skip 1046件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $132.51

## 4. Latest Market Context

- 更新: 2026-06-02T00:58:54.804706+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=71274.9
- Funnel: target 774 → liquid 147 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.4 >= 65=1, 4h RSI 68.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +70.95% | $8,836,440.57 |
| SLX/USDT:USDT | +14.57% | $12,644,325.96 |
| UB/USDT:USDT | +12.76% | $2,446,434.73 |
| WLD/USDT:USDT | +12.75% | $139,419,165.90 |
| PLAY/USDT:USDT | +9.86% | $7,540,521.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.13% | +4.29% |
| LAB/USDT:USDT | below_1h_threshold | +2.59% | +2.75% |
| SLX/USDT:USDT | below_1h_threshold | +1.82% | +1.99% |
| NEX/USDT:USDT | below_1h_threshold | +1.60% | +1.76% |
| BEAT/USDT:USDT | below_1h_threshold | +1.24% | +1.40% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
