# Decision Report

- generated_at: 2026-05-30T09:29:48.457865+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5114**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.46% / filled 20/20。**
- 全期間 MARKET基準: n=5114, expectancy=-0.06%
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
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.44% | **+1.22%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.12% | **+1.01%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.99% | **+0.64%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.82% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.95** / 初期 $100.00 (+26.95%)
- 確定: 769件 (Win 180 / Loss 231 / Flat 358) / skip 906件
- 成長率目線: 平均log +0.000310 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.95

## 4. Latest Market Context

- 更新: 2026-05-30T09:29:46.159040+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=73530.0
- Funnel: target 773 → liquid 131 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NFP/USDT:USDT | +68.79% | $1,442,415.18 |
| HEI/USDT:USDT | +50.88% | $16,382,543.88 |
| VTHO/USDT:USDT | +30.28% | $1,340,237.93 |
| LAB/USDT:USDT | +21.24% | $124,160,701.62 |
| XLM/USDT:USDT | +15.44% | $440,090,044.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NFP/USDT:USDT | below_1h_threshold | +4.27% | +4.22% |
| ALLO/USDT:USDT | below_1h_threshold | +2.17% | +2.12% |
| ALGO/USDT:USDT | below_1h_threshold | +1.74% | +1.69% |
| LIT/USDT:USDT | below_1h_threshold | +1.70% | +1.65% |
| VET/USDT:USDT | below_1h_threshold | +1.60% | +1.55% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
