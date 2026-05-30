# Decision Report

- generated_at: 2026-05-30T10:00:16.511928+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5115**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.46% / filled 20/20。**
- 全期間 MARKET基準: n=5115, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +5.96% | **+0.89%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.49% | **+0.49%** |
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.55% | **+1.31%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.49% | **+1.04%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.12% | **+1.01%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.92% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.75** / 初期 $100.00 (+27.75%)
- 確定: 770件 (Win 181 / Loss 231 / Flat 358) / skip 906件
- 成長率目線: 平均log +0.000318 / 幾何平均 +0.032% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NFP/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $127.75

## 4. Latest Market Context

- 更新: 2026-05-30T10:00:14.381188+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=73576.9
- Funnel: target 773 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NFP/USDT:USDT | +78.53% | $1,968,677.41 |
| HEI/USDT:USDT | +33.92% | $16,929,209.42 |
| VTHO/USDT:USDT | +30.63% | $1,408,444.61 |
| LAB/USDT:USDT | +23.94% | $125,088,386.41 |
| ALGO/USDT:USDT | +15.83% | $7,762,093.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIGHT/USDT:USDT | below_1h_threshold | +3.10% | +3.10% |
| LIT/USDT:USDT | below_1h_threshold | +0.68% | +0.68% |
| ALLO/USDT:USDT | below_1h_threshold | +0.44% | +0.44% |
| CRWVSTOCK/USDT:USDT | below_1h_threshold | +0.27% | +0.27% |
| ALGO/USDT:USDT | below_1h_threshold | +0.23% | +0.23% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
