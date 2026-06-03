# Decision Report

- generated_at: 2026-06-03T18:40:38.785583+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5571**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.70% / filled 20/20。**
- 全期間 MARKET基準: n=5571, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.84% | **+0.96%** |
| ASK | 20/20 | 100.0% | +0.80% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.56% | **+0.45%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +5.00% | **+2.22%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.95% | **+0.81%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.96% | **+0.79%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.43% | **+0.64%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.75% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$97.09** / 初期 $100.00 (-2.91%)
- 確定トレード: 92件 (TP 27 / SL 62 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.09
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1004件 (Win 239 / Loss 312 / Flat 453) / skip 1128件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-03T18:40:35.671716+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=65954.3
- Funnel: target 768 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +51.00% | $9,673,818.49 |
| STO/USDT:USDT | +33.97% | $1,267,195.69 |
| BP/USDT:USDT | +9.93% | $1,436,992.85 |
| LAB/USDT:USDT | +8.47% | $272,187,277.27 |
| MAGMA/USDT:USDT | +7.44% | $3,661,093.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.08% | +4.05% |
| US/USDT:USDT | below_1h_threshold | +3.88% | +3.85% |
| EPIC/USDT:USDT | below_1h_threshold | +3.38% | +3.35% |
| LIT/USDT:USDT | below_1h_threshold | +2.39% | +2.36% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.23% | +2.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
