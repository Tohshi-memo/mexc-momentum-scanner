# Decision Report

- generated_at: 2026-06-11T15:12:33.091506+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6368**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6368, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.47% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.59% | **+1.59%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.12% | **+1.56%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.02% | **+1.32%** |
| ASK_LONG | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.86% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$154.19** / 初期 $100.00 (+54.19%)
- 確定: 1288件 (Win 331 / Loss 406 / Flat 551) / skip 1641件
- 成長率目線: 平均log +0.000336 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPACE/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $154.19

## 4. Latest Market Context

- 更新: 2026-06-11T15:12:26.976267+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=62716.7
- Funnel: target 782 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +108.22% | $87,170,173.06 |
| H/USDT:USDT | +96.45% | $29,781,116.02 |
| AIO/USDT:USDT | +70.16% | $9,102,221.90 |
| BEAT/USDT:USDT | +62.41% | $236,836,993.87 |
| COLLECT/USDT:USDT | +50.69% | $2,410,740.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPACE/USDT:USDT | below_1h_threshold | +4.22% | +4.19% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.99% | +2.96% |
| H/USDT:USDT | below_1h_threshold | +2.09% | +2.06% |
| ID/USDT:USDT | below_1h_threshold | +1.79% | +1.77% |
| VELVET/USDT:USDT | below_1h_threshold | +1.65% | +1.62% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
