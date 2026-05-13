# Decision Report

- generated_at: 2026-05-13T21:03:02.818818+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4252**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.84% / filled 20/20。**
- 全期間 MARKET基準: n=4252, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.88% | **+0.79%** |
| LIMIT_BB3S | 3/14 | 21.4% | +1.42% | **+0.30%** |
| ASK | 20/20 | 100.0% | +0.22% | **+0.22%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.96% | **+0.78%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.59% | **+0.53%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$98.19** / 初期 $100.00 (-1.81%)
- 確定トレード: 39件 (TP 10 / SL 26 / EXP 3)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.19
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 342件 (Win 94 / Loss 125 / Flat 123) / skip 471件
- 成長率目線: 平均log +0.000513 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-13T21:02:59.363461+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=79604.9
- Funnel: target 759 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +19.42% | $1,506,482.50 |
| CSCOSTOCK/USDT:USDT | +17.26% | $2,787,688.83 |
| BEAT/USDT:USDT | +14.75% | $2,615,431.23 |
| UP/USDT:USDT | +14.39% | $4,692,457.43 |
| BB/USDT:USDT | +12.42% | $1,859,507.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CSCOSTOCK/USDT:USDT | below_1h_threshold | +1.99% | +2.08% |
| IRYS/USDT:USDT | below_1h_threshold | +0.69% | +0.77% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +0.56% | +0.64% |
| BSB/USDT:USDT | below_1h_threshold | +0.50% | +0.58% |
| COLLECT/USDT:USDT | below_1h_threshold | +0.47% | +0.55% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
