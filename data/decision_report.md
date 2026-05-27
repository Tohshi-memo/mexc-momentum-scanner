# Decision Report

- generated_at: 2026-05-27T12:26:19.883932+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4926**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.01% / filled 20/20。**
- 全期間 MARKET基準: n=4926, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.01% | **+1.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.10% | **+1.10%** |
| MARKET | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.84% | **+0.76%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.63% | **+0.47%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.95% | **+0.57%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.33% | **+0.33%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.21% | **+0.19%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.10% | **+0.07%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.07% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 684件 (Win 172 / Loss 220 / Flat 292) / skip 803件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-27T12:26:17.269306+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=75909.8
- Funnel: target 775 → liquid 144 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +18.90% | $16,773,375.92 |
| RIF/USDT:USDT | +18.01% | $1,340,758.77 |
| ALT/USDT:USDT | +15.40% | $2,670,834.57 |
| BEAT/USDT:USDT | +15.27% | $19,831,242.41 |
| LUNC/USDT:USDT | +14.57% | $15,141,486.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AR/USDT:USDT | below_1h_threshold | +2.53% | +2.30% |
| REQ/USDT:USDT | below_1h_threshold | +2.39% | +2.16% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +2.36% | +2.13% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.04% | +1.81% |
| USELESS/USDT:USDT | below_1h_threshold | +2.00% | +1.77% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
