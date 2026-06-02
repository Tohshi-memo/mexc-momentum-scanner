# Decision Report

- generated_at: 2026-06-02T12:49:57.832911+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5452**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=5452, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.42% | **+1.42%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.72% | **+0.61%** |
| LIMIT_4PCT | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_BB3S | 6/15 | 40.0% | +0.94% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +0.22% | **+0.13%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.09% | **+0.06%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +0.07% | **+0.02%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | -0.10% | **-0.04%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.38% | **-0.28%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 87件 (TP 25 / SL 59 / EXP 3)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.99** / 初期 $100.00 (+31.99%)
- 確定: 964件 (Win 226 / Loss 293 / Flat 445) / skip 1049件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.99

## 4. Latest Market Context

- 更新: 2026-06-02T12:49:55.497821+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.46% price=69113.3
- Funnel: target 773 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +35.35% | $3,837,343.56 |
| USELESS/USDT:USDT | +30.48% | $2,815,638.32 |
| LAB/USDT:USDT | +28.49% | $175,382,028.79 |
| CLO/USDT:USDT | +26.78% | $1,127,060.90 |
| PIEVERSE/USDT:USDT | +24.20% | $3,886,840.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.68% | +5.14% |
| RIF/USDT:USDT | below_1h_threshold | +4.33% | +4.79% |
| H/USDT:USDT | below_1h_threshold | +3.90% | +4.36% |
| UB/USDT:USDT | below_1h_threshold | +3.74% | +4.19% |
| CLO/USDT:USDT | below_1h_threshold | +2.94% | +3.40% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
