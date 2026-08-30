# Decision Report

- generated_at: 2026-08-30T05:46:23.425308+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13026**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13026, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.75% | **-1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 13/17 | 76.5% | +1.40% | **+1.07%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.26% | **+0.57%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.06% | **+0.42%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.17% | **+0.09%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +3.00% | **+1.35%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.58% | **+1.16%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.44% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$789.14** / 初期 $100.00 (+689.14%)
- 確定: 4796件 (Win 1461 / Loss 1577 / Flat 1758) / skip 4791件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKR/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $789.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.30** / 初期 $100.00 (+74.30%)
- 確定: 2110件 (Win 591 / Loss 514 / Flat 1005) / skip 4327件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0469 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKR/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $174.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.23** / 初期 $100.00 (+17.23%)
- 確定: 2069件 (Win 608 / Loss 802 / Flat 659) / pending 2件 / skip 2425件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000313 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.23

## 6. Latest Market Context

- 更新: 2026-08-30T05:46:11.081915+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=78100.0
- Funnel: target 1023 → liquid 117 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +84.10% | $32,946,591.30 |
| NIULAI/USDT:USDT | +62.09% | $2,652,217.94 |
| FONE/USDT:USDT | +54.90% | $1,417,473.30 |
| PONS/USDT:USDT | +41.67% | $1,537,427.22 |
| SKR/USDT:USDT | +38.43% | $1,651,909.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +4.89% | +4.86% |
| BTW/USDT:USDT | below_1h_threshold | +3.63% | +3.61% |
| TUT/USDT:USDT | below_1h_threshold | +3.60% | +3.57% |
| BEAT/USDT:USDT | below_1h_threshold | +3.58% | +3.55% |
| HNT/USDT:USDT | below_1h_threshold | +2.56% | +2.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
