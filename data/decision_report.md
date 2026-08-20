# Decision Report

- generated_at: 2026-08-20T21:31:16.488368+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12102**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.63% / filled 20/20。**
- 全期間 MARKET基準: n=12102, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.63% | **+0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +0.98% | **+0.98%** |
| MARKET | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +5.21% | **+3.47%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.52% | **+1.37%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.71% | **+0.50%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$648.62** / 初期 $100.00 (+548.62%)
- 確定: 4315件 (Win 1324 / Loss 1411 / Flat 1580) / skip 4348件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AVAAI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $648.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3691件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1244 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.27** / 初期 $100.00 (+17.27%)
- 確定: 1789件 (Win 531 / Loss 679 / Flat 579) / pending 3件 / skip 1782件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000163 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.27

## 6. Latest Market Context

- 更新: 2026-08-20T21:31:07.942211+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=72656.7
- Funnel: target 1011 → liquid 198 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +60.84% | $2,992,097.59 |
| ONG/USDT:USDT | +50.46% | $11,444,630.68 |
| ONT/USDT:USDT | +26.59% | $2,116,932.87 |
| PEOPLE/USDT:USDT | +16.19% | $3,200,935.64 |
| ENA/USDT:USDT | +9.78% | $33,578,051.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.93% | +3.91% |
| LAB/USDT:USDT | below_1h_threshold | +2.40% | +2.37% |
| NEIROCTO/USDT:USDT | below_1h_threshold | +1.52% | +1.49% |
| BRETT/USDT:USDT | below_1h_threshold | +1.28% | +1.26% |
| TAO/USDT:USDT | below_1h_threshold | +1.23% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
