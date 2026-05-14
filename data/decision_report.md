# Decision Report

- generated_at: 2026-05-14T03:48:09.123711+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4269**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.49% / filled 20/20。**
- 全期間 MARKET基準: n=4269, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+1.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.49% | **+1.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.50% | **+1.50%** |
| MARKET | 20/20 | 100.0% | +1.49% | **+1.49%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.55% | **+1.32%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.52% | **+0.91%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.25% | **+0.87%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +2.90% | **+1.45%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.38% | **+0.62%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.43% | **+0.37%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.82% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$97.21** / 初期 $100.00 (-2.79%)
- 確定トレード: 41件 (TP 10 / SL 28 / EXP 3)
- 最新: SAGA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 343件 (Win 94 / Loss 125 / Flat 124) / skip 487件
- 成長率目線: 平均log +0.000512 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-14T03:48:05.738024+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=79103.9
- Funnel: target 765 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CSCOSTOCK/USDT:USDT | +22.73% | $4,909,079.46 |
| UP/USDT:USDT | +22.31% | $5,035,428.42 |
| SAGA/USDT:USDT | +20.81% | $16,748,429.36 |
| TROLLSOL/USDT:USDT | +20.78% | $1,950,226.21 |
| IRYS/USDT:USDT | +14.31% | $6,416,961.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.18% | +3.47% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.02% | +2.31% |
| AIN/USDT:USDT | below_1h_threshold | +1.98% | +2.26% |
| UP/USDT:USDT | below_1h_threshold | +1.73% | +2.01% |
| LAB/USDT:USDT | below_1h_threshold | +1.55% | +1.84% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
