# Decision Report

- generated_at: 2026-05-30T00:35:05.195707+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5081**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.07% / filled 20/20。**
- 全期間 MARKET基準: n=5081, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+2.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.15% | **+2.15%** |
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.58% | **+1.27%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.93% | **+0.37%** |
| LIMIT_BB3S | 7/18 | 38.9% | +0.75% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.70% | **+0.51%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.56% | **+0.11%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.71% | **-0.32%** |

## 2. $100 Live Portfolio

- 残高: **$98.60** / 初期 $100.00 (-1.40%)
- 確定トレード: 74件 (TP 22 / SL 49 / EXP 3)
- 最新: LIT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 742件 (Win 175 / Loss 226 / Flat 341) / skip 900件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-30T00:35:00.453728+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=73395.4
- Funnel: target 773 → liquid 147 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XLM/USDT:USDT | +22.00% | $407,634,993.95 |
| OL/USDT:USDT | +16.61% | $1,465,578.50 |
| LAB/USDT:USDT | +14.87% | $131,031,803.93 |
| BASED/USDT:USDT | +14.49% | $2,478,336.74 |
| HBAR/USDT:USDT | +12.29% | $33,042,730.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HBAR/USDT:USDT | below_1h_threshold | +4.74% | +4.79% |
| SEI/USDT:USDT | below_1h_threshold | +3.14% | +3.18% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.14% | +2.18% |
| BSB/USDT:USDT | below_1h_threshold | +1.76% | +1.80% |
| ALGO/USDT:USDT | below_1h_threshold | +1.14% | +1.18% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
