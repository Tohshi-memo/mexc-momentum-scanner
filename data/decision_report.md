# Decision Report

- generated_at: 2026-06-16T20:35:27.918942+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6885**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=6885, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.72% | **+0.69%** |
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.31% | **+0.46%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.31% | **+0.22%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.28% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.84% | **+0.63%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| MARKET_LONG | 20/20 | 100.0% | +0.09% | **+0.09%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.07% | **+0.06%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.01% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$184.51** / 初期 $100.00 (+84.51%)
- 確定: 1758件 (Win 464 / Loss 553 / Flat 741) / skip 1688件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $184.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.68** / 初期 $100.00 (-2.32%)
- 確定: 160件 (Win 29 / Loss 31 / Flat 100) / skip 136件
- 成長率目線: 平均log -0.000147 / 幾何平均 -0.015% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0238 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $97.68

## 5. Latest Market Context

- 更新: 2026-06-16T20:35:22.861839+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=65748.7
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +18.09% | $28,036,956.93 |
| BLESS/USDT:USDT | +15.41% | $1,567,697.63 |
| PLAY/USDT:USDT | +14.45% | $1,535,773.51 |
| ESPORTS/USDT:USDT | +13.05% | $1,697,239.85 |
| SENT/USDT:USDT | +12.55% | $1,158,742.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.74% | +4.59% |
| BSB/USDT:USDT | below_1h_threshold | +4.31% | +4.16% |
| VELVET/USDT:USDT | below_1h_threshold | +3.14% | +3.00% |
| BLESS/USDT:USDT | below_1h_threshold | +2.82% | +2.67% |
| UAI/USDT:USDT | below_1h_threshold | +2.58% | +2.43% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
