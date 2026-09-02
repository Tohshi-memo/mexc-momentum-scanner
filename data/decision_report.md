# Decision Report

- generated_at: 2026-09-02T22:47:01.914340+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13397**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13397, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 14/20 | 70.0% | +2.05% | **+1.44%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.99% | **+0.89%** |
| LIMIT_BB3S | 5/16 | 31.2% | +1.30% | **+0.41%** |
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.05% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +4.48% | **+2.01%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.37% | **+0.95%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.22% | **+0.85%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.09% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$870.32** / 初期 $100.00 (+770.32%)
- 確定: 4994件 (Win 1514 / Loss 1638 / Flat 1842) / skip 4964件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $870.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.60** / 初期 $100.00 (+84.60%)
- 確定: 2372件 (Win 671 / Loss 576 / Flat 1125) / skip 4436件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0875 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $184.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.16** / 初期 $100.00 (+14.16%)
- 確定: 2107件 (Win 614 / Loss 827 / Flat 666) / pending 5件 / skip 2760件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000329 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.16

## 6. Latest Market Context

- 更新: 2026-09-02T22:46:50.531012+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=77068.2
- Funnel: target 1044 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +60.31% | $70,789,663.45 |
| SNOWSTOCK/USDT:USDT | +21.50% | $1,373,755.05 |
| PONS/USDT:USDT | +20.83% | $3,282,202.61 |
| BTW/USDT:USDT | +17.92% | $11,157,503.90 |
| EGLD/USDT:USDT | +14.33% | $6,995,852.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +3.75% | +3.99% |
| CASHCAT/USDT:USDT | below_1h_threshold | +2.97% | +3.21% |
| NIULAI/USDT:USDT | below_1h_threshold | +2.15% | +2.39% |
| 4/USDT:USDT | below_1h_threshold | +2.05% | +2.29% |
| KORU/USDT:USDT | below_1h_threshold | +1.70% | +1.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
