# Decision Report

- generated_at: 2026-06-02T10:32:58.124672+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5442**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=5442, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.47% | **+1.47%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_4PCT | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.59% | **+0.42%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +1.11% | **+0.33%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | -0.10% | **-0.04%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.50% | **-0.08%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | -0.38% | **-0.28%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.80% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$97.10** / 初期 $100.00 (-2.90%)
- 確定トレード: 86件 (TP 25 / SL 58 / EXP 3)
- 最新: LIT/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.30** / 初期 $100.00 (+33.30%)
- 確定: 954件 (Win 224 / Loss 288 / Flat 442) / skip 1049件
- 成長率目線: 平均log +0.000301 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $133.30

## 4. Latest Market Context

- 更新: 2026-06-02T10:32:54.764252+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.33% price=69618.7
- Funnel: target 772 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +42.26% | $2,924,883.42 |
| MRVLSTOCK/USDT:USDT | +28.95% | $4,921,391.94 |
| ESPORTS/USDT:USDT | +25.47% | $12,890,687.89 |
| EPIC/USDT:USDT | +24.50% | $2,373,679.53 |
| UB/USDT:USDT | +24.13% | $3,061,377.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +4.38% | +4.05% |
| USELESS/USDT:USDT | below_1h_threshold | +3.76% | +3.44% |
| WLD/USDT:USDT | below_1h_threshold | +2.43% | +2.10% |
| ARKM/USDT:USDT | below_1h_threshold | +2.28% | +1.95% |
| ICP/USDT:USDT | below_1h_threshold | +2.24% | +1.91% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
